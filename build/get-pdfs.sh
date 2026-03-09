# Get all PDF paths from the repository
curl -H "Authorization: token $GITHUB_TOKEN" -s "https://api.github.com/repos/8-chems/myportfolio-src/git/trees/main?recursive=1" \
  | jq -r '.tree[]? | select(.path | endswith(".pdf")) | .path' \
  | while read -r pdf_path; do
      # Create directory structure
      mkdir -p "pdfs/$(dirname "$pdf_path")"
      # Download the file
      curl -L -o "pdfs/$pdf_path" \
        "https://raw.githubusercontent.com/8-chems/myportfolio-src/main/$pdf_path"
    done