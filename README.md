# rr-webapi

Python client library for RaceResult Web API

## Installation

```bash
pip install rr-webapi
```

## Quick Start

```python
from rr_webapi import API
import os

# Create API client
api = API("events.raceresult.com", use_https=True)

# Login with API key
api.public.login(api_key=os.getenv("RACERESULT_API_KEY"))

try:
    # Get your events
    events = api.public.event_list()
    print(f"You have {len(events)} events")
    
    # Open an event
    if events:
        event_api = api.event_api(events[0].id)
        
        # Get participants
        participants = event_api.data.list([
            "ID", "BIB", "FIRSTNAME", "LASTNAME", "CONTEST.NAME"
        ])
        print(f"Event has {len(participants)} participants")

finally:
    # Always logout
    api.public.logout()
```

## Features

- 🐍 **Pythonic API design** with dataclasses
- 🔄 **Session management** with automatic cleanup
- 📦 **Modular design** with organized endpoints
- 🛡️ **Type hints** for better IDE support
- 🔧 **Easy configuration** with environment variables

## API Coverage

- **Authentication**: Login/logout with API keys or username/password
- **Events**: List and access event data
- **Participants**: Manage participant information  
- **Raw Data**: Access timing data and splits
- **Contests**: Handle contest management
- **Data**: Advanced querying and filtering

## Requirements

- Python 3.7+
- requests
- python-dateutil
- python-dotenv

## License

GPL-3.0 © SPTiming

## Support

For issues and questions, please visit our [GitHub Issues](https://github.com/SPTiming/python-rr-webapi/issues).
