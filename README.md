This repo provide a tool to convert a Huggingface model into GGUF file.
It follows the instruction at https://github.com/ggerganov/llama.cpp/discussions/2948

#### Install dependencies
- Run `pip install -r requirements.text`
- Clone `llama.ccp` repo `git clone https://github.com/ggerganov/llama.cpp.git`
- Install dependencies for llama.ccp: `pip install -r llama.cpp/requirements.txt`

#### Convert model
- Run 
  ```
    python llama.cpp/convert-hf-to-gguf.py <model_path> \
    --outfile <output_file>.gguf \
    --outtype <quant_type {f16,f32}>
  ```

- Example: 

  ```
    python llama.cpp/convert-hf-to-gguf.py huggingface_models/vince62s-phi2-psy \
    --outfile vince62s-phi2-psy_q8.gguf \
    --outtype f16
  ```
#### Quantize
##### Build llama.ccp
  - In llama.cpp run `make`

##### Quantize the model to 4-bits (using Q4_K_M method)
```
llama.cpp/quantize vince62s-phi2-psy.gguf .vince62s-phi2-psy-Q4_K_M.gguf Q4_K_M
``` 

##### Update the gguf filetype to current version if older version is now unsupported
```
llama.cpp/quantize vince62s-phi2-psy-Q4_K_M.gguf .vince62s-phi2-psy-Q4_K_M.gguf
```

#### Run GGUF file with llama.cpp
- Example: `llama.cpp/main -m vince62s-phi2-psy_Q4_K_M.gguf -cml`

#### Run GGUF file with Ollama
- Create Modelfile with, e.g.
  `FROM ./vince62s-phi-2-psy_f16.gguf`
- Create the model in ollama `ollama create phi-2_f16 -f Modelfile`
- Run the model with ollama `ollama run phi2_f16`

### Push models to Hugging Face
- You need to use a Hugging Face Write Token to push your files to Hugging Face
- `export HUGGING_FACE_HUB_TOKEN=<Your_HF_token>`
- Update `upload_hf.py` with your model_id, etc. Then run `python upload_hf.py`
