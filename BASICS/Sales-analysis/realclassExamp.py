class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=1000):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1/chat/completions"
       
        
    #create different configurations for different models
    #using positional for required arg,named for optional parameters
    dev_config=APIConfig("sk-prod-key", model="gpt-4", max_tokens=5)
    
    
    #Access the configuration
    print(dev_config.api_key)
    print(dev_config.model)
    print(dev_config.max_tokens)
    print(dev_config.base_url)

    
    
    

#access