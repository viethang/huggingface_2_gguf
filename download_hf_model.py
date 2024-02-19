# Script to download a HuggingFace model
# Usage `python download.py model_id local_dir`

from huggingface_hub import snapshot_download
import sys

def download_model(model_id: str, local_dir: str):

  snapshot_download(repo_id=model_id, local_dir=local_dir,
                  local_dir_use_symlinks=False, revision="main")
  
if __name__ == "__main__":
  model_id = sys.argv[1]
  local_dir = sys.argv[2]

  download_model(model_id, local_dir)  
