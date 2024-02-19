from huggingface_hub import HfApi
api = HfApi()


def push_to_hf(model_id: str, model_base_name: str, model_dir: str, versions: list[str]):
    api.create_repo(model_id, exist_ok=True, repo_type="model")
    model_file_names = [f"{model_base_name}{version}.gguf" for version in versions]
    for model_file in model_file_names:
        api.upload_file(
            path_or_fileobj=f"{model_dir}/{model_file}",
            path_in_repo=model_file,
            repo_id=model_id,
    )
        
if __name__ == "__main__":
    print("Define model_id, model_dir, model_base_name, versions and run.")

    # model_id = "viethang/vince62s-phi-2-psy-GGUF"
    # model_dir = 'GGUF_models/vince62s-phi-2-psy'
    # model_base_name = 'vince62s-phi-2-psy_'
    # versions = ['Q4_0', 'Q4_K_M', 'Q4_K_S', 'Q5_K_M', 'Q5_K_S', 'Q6_K', 'Q8_0']
    # push_to_hf(model_id=model_id, model_base_name=model_base_name, model_dir=model_dir, versions=versions)



