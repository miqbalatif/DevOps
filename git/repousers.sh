#!/bin/bash

################
# Author: atif
# Date: 2024-03-24
# Description: This script takes a GitHub username and repository name as arguments, and prints information about the repository.
################

# Prompt the user for their GitHub username
read -p "Enter your GitHub username: " username

# Prompt the user for their GitHub token
read -s -p "Enter your GitHub token: " token
echo

# Read the username and repository arguments
repo_username=$1
repo_name=$2

# Make a GET request to the GitHub API to get the repository information
response=$(curl -s -H "Authorization: token $token" "https://api.github.com/repos/$repo_username/$repo_name")

# Check if the repository was not found or if there was an error
if [[ "$(echo "$response" | jq -r '.message')" == "Not Found" ]]; then
	    echo "Repository not found."
	        exit 1
	elif [[ "$(echo "$response" | jq -r '.message')" != "null" ]]; then
		    echo "Error: $(echo "$response" | jq -r '.message')"
		        exit 1
fi

# Print the repository information
echo "Repository: $repo_username/$repo_name"
echo "Description: $(echo "$response" | jq -r '.description')"
echo "Language: $(echo "$response" | jq -r '.language')"
echo "Stars: $(echo "$response" | jq -r '.stargazers_count')"
echo "Forks: $(echo "$response" | jq -r '.forks_count')"

# Make a GET request to the GitHub API to get the contributors information
contributors_response=$(curl -s -H "Authorization: token $token" "https://api.github.com/repos/$repo_username/$repo_name/contributors")

# Check if the request was successful
if [[ "$(echo "$contributors_response" | jq -r 'type')" == "array" ]]; then
	    # Print the contributors information
	        echo "Contributors:"
		    echo "$(echo "$contributors_response" | jq -r '.[].login')"
	    else
		        echo "Contributors not found."
			    exit 1
fi
