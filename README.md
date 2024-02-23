# Tonic Validate for pull requests (PRs)
Github action to run Tonic Validate evaluation on a PR.  This Github action takes advantage of the open source [Tonic Validate library](https://github.com/TonicAI/tonic_validate).

![image](https://github.com/TonicAI/tonic_validate_pr_action/assets/9391841/f7672f8f-ba83-4fd5-9a4d-afd54d36f75f)


# Setup

To kick off a Tonic Validate evaluation on a PR, add the sample workflow to .github/workflows.

```yml
name: Tonic Validate
on: [pull_request]

jobs:
  tonic-validate:
    runs-on: ubuntu-latest
    name: Tonic Validate
    env:
      OPENAI_API_KEY:  ${{ secrets.OPENAI_API_KEY }}
      AZURE_OPENAI_KEY: ${{ secrets.AZURE_OPENAI_KEY}}
      AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT}}
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4      
      - name: Validate
        uses: TonicAI/tonic_validate_pr_action@v0.1.0
        with:
          llm_response_path: <Path to Q&A for Evaluation>
```

This workflow requires that you do one of the following:

- Set an OpenAI API key
- Set both an Azure API key and an Azure Endpoint URL

You also must provide a value for `llm_response_path`, which is the path (relative to the root of your repository) to a JSON file that contains the questions and optional context and reference answers for Tonic Validate to evaluate. 

Here is a sample set of questions and answers:

```json
[
    {"llm_answer":"Paris", "benchmark_item":{"question":"What is the capital of Paris", "answer":"Paris"}},
    {"llm_answer":"Berlin", "benchmark_item":{"question":"What is the capital of Germany", "answer":"Berlin"}},
    {"llm_answer":"Sam Altman is the CEO of OpenAI", "llm_context_list": ["Sam Altman has been the CEO of OpenAI since 2019."], "benchmark_item":{"question":"Who is the CEO of OpenAI?", "answer":"Sam Altman"}},
]
```
