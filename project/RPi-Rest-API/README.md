# RPi-Rest-API

In the requirements.txt  you can find what you need for the Project to work.

For Example Pip:

```bash
pip install -r requirements_api.txt
```


## api request mit Key 

```powershell

PS C:\Users\user\projects\Rapi_API_lol\RPi-Rest-API> $response = Invoke-RestMethod `
>>   -Uri "http://127.0.0.1:5000/api/plants/" `
>>   -Headers @{
>>     "X-API-Key" = "abc"
>>   }
PS C:\Users\user\projects\Rapi_API_lol\RPi-Rest-API> $response | ConvertTo-Json -Depth 10
[
    {
        "id":  1,
        "plant_name":  "Test Plant 1",
        "waterlevel":  1
    },
    {
        "id":  2,
        "plant_name":  "Test Plant 2",
        "waterlevel":  0
    },
    {
        "id":  3,
        "plant_name":  "Test Plant 3",
        "waterlevel":  1
    },
    {
        "id":  4,
        "plant_name":  "Test Plant 4",
        "waterlevel":  0
    }
]

```