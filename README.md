# Tonic Validate for PRs
Github action for running Tonic Validate evaluation on a PR

# Setup

The sample workflow can be added to .github/workflows and is all that is needed to kickoff a Tonic Validate evaluation on a PR.

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

This workflow requires that you either set an OpenAI Api Key OR you set both an Azure API key and Azure Endpoint URL.  Additionally, you need to provide a value for llm_response_path which is the path (relative to the root of your repository) to a JSON file containing the questions and optional context and reference answers for which you wish evaluate with Tonic Validate. 

Below is a sample set of questions and answers

```json
[
    {"llm_answer":"Paris", "benchmark_item":{"question":"What is capital of Paris", "answer":"Paris"}},
    {"llm_answer":"Berlin", "benchmark_item":{"question":"What is capital of Germany", "answer":"Berlin"}},
    {"llm_answer":"Sam Altman is the CEO of OpenAI", "llm_context_list": ["Sam Altman has been the CEO of OpenAI since 2019."], "benchmark_item":{"question":"Who is the CEO of OpenAI?", "answer":"Sam Altman"}},
]
```
