/********************************************************************************
 * Copyright (c) 2021,2022 Mercedes-Benz Tech Innovation Gmbh
 * Copyright (c) 2021,2022 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License, Version 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************/

package main

import (
	"context"
	"fmt"
	"github.com/google/go-github/v48/github"
	"golang.org/x/oauth2"
	"helm.sh/helm/v3/pkg/repo"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
	"time"
)

func getAuthenticatedClient(ctx context.Context) *github.Client {
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: os.Getenv("GH_TOKEN")},
	)
	tc := oauth2.NewClient(ctx, ts)

	return github.NewClient(tc)
}

func getOrgRepos(ctx context.Context, gitOwner string, client *github.Client) ([]*github.Repository, *github.Response, error) {
	opt := &github.RepositoryListByOrgOptions{
		Type: "all",
	}
	repos, response, err := client.Repositories.ListByOrg(ctx, gitOwner, opt)
	return repos, response, err
}

func downloadProductHelmRepoIndex(ctx context.Context, client *github.Client, gitOwner string, gitRepo string) string {
	pageInfo, _, _ := client.Repositories.GetPagesInfo(ctx, gitOwner, gitRepo)
	fullURLFile := *pageInfo.HTMLURL + "index.yaml"
	fileName := gitRepo + "-index.yaml"

	file, err := os.Create(fileName)
	if err != nil {
		log.Fatal(err)
	}

	response, _ := http.Get(fullURLFile)
	if response.StatusCode == 200 {
		_, _ = io.Copy(file, response.Body)
		response.Body.Close()
		file.Close()
	}
	return fileName
}

func buildHelmRepoIndex(indexFile string, mergeIndexFile string) {
	repoFile, err := repo.LoadIndexFile(indexFile)
	if err != nil {
		log.Fatal(err)
	}

	if fileStat, _ := os.Stat(mergeIndexFile); fileStat.Size() > 0 {
		newIndex, err := repo.LoadIndexFile(mergeIndexFile)
		if err != nil {
			log.Fatal(err)
		}
		repoFile.Merge(newIndex)
		repoFile.Generated = time.Now()
		repoFile.WriteFile(indexFile, 0644)
		//os.Remove(mergeIndexFile)
	}
}

const centralHelmIndex = "../../charts/dev/index.yaml"
const gitOwner = "catenax-ng"

func main() {
	ctx := context.Background()
	client := getAuthenticatedClient(ctx)
	repos, _, _ := getOrgRepos(ctx, gitOwner, client)

	for i, gitRepo := range repos {
		var gitRepoHelmIndex string

		//check gh pages configured for repo
		_, response, _ := client.Repositories.GetBranch(ctx, gitOwner, *gitRepo.Name, "gh-pages", false)

		if response.StatusCode == 200 {
			if !strings.Contains(*gitRepo.Name, "k8s-") {
				fmt.Println(i, *gitRepo.Name)
				gitRepoHelmIndex = downloadProductHelmRepoIndex(ctx, client, gitOwner, *gitRepo.Name)
				buildHelmRepoIndex(centralHelmIndex, gitRepoHelmIndex)
				os.Remove(gitRepoHelmIndex)
			}
		}
	}
}
