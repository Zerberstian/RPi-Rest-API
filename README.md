# RPi-Rest-API

## Installation and requirements

### best way to get them Project to your PC:

```bash
git clone URL <- placeholder
```

### requirements:

note:
For our API requirements to work you need to be in venv so 

--

In the requirements_api.txt  you can find what you need for the Project to work.

using Pip:

```bash
pip install -r requirements_api.txt
```
note:
requests ist not installed in rpi ans Not in req.txt

```bash
pip install requests
```
 
--

## api request with example Key

here you do tehe request and save the API Output to a Variable: 

```powershell

PS C:\Users\user\projects\Rapi_API_lol\RPi-Rest-API> $response = Invoke-RestMethod `
>>   -Uri "http://127.0.0.1:5000/api/plants/" `
>>   -Headers @{
>>     "X-API-Key" = "abc"
>>   }

```

get what was saved to the Variable:

```powershell
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