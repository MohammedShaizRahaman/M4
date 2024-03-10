import requests

def parse_swagger(swagger_url):
    try:
        response = requests.get(swagger_url)
        if response.status_code == 200:
            swagger_data = response.json()
            paths = swagger_data.get('paths', {})
            if paths:
                print("Endpoints:")
                for path, methods in paths.items():
                    print(path)
            else:
                print("No endpoints found in Swagger JSON.")
        else:
            print("Failed to fetch Swagger JSON:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Example usage
swagger_url = "http://petstore.swagger.io/v2/swagger.json"
parse_swagger(swagger_url)
