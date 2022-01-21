# Baicells BOSS Python
Python support for Baicells BOSS API

## Table of Contents
- [Baicells BOSS Python](#baicells-boss-python)
  - [Table of Contents](#table-of-contents)
    - [Dependencies](#dependencies)
  - [Basic Usage](#basic-usage)
  - [Query Subscriber](#query-subscriber)
    - [Query by ID](#query-by-id)
      - [Arguments](#arguments)
      - [Example](#example)
    - [Query by IMSI](#query-by-imsi)
      - [Arguments](#arguments-1)
      - [Example](#example-1)
  - [Create Subscriber](#create-subscriber)
    - [Create a Single Subscriber](#create-a-single-subscriber)
      - [Arguments](#arguments-2)
      - [Example](#example-2)
    - [Bulk Create Subscribers](#bulk-create-subscribers)
      - [Arguments](#arguments-3)
      - [Example](#example-3)
  - [Bind Service Plan](#bind-service-plan)
      - [Arguments](#arguments-4)
      - [Example](#example-4)
  - [Bind IMSI](#bind-imsi)
      - [Arguments](#arguments-5)
      - [Example](#example-5)
  - [Unbind IMSI](#unbind-imsi)
      - [Arguments](#arguments-6)
      - [Example](#example-6)
  - [Activate Subscriber](#activate-subscriber)
    - [Activate Single Subscriber](#activate-single-subscriber)
      - [Arguments](#arguments-7)
      - [Example](#example-7)
    - [Bulk Activate Subscribers](#bulk-activate-subscribers)
      - [Arguments](#arguments-8)
      - [Example](#example-8)
  - [Deactivate Subscriber](#deactivate-subscriber)
    - [Deactivate Single Subscriber](#deactivate-single-subscriber)
      - [Arguments](#arguments-9)
      - [Example](#example-9)
    - [Bulk Deactivate Subscribers](#bulk-deactivate-subscribers)
      - [Arguments](#arguments-10)
      - [Example](#example-10)
  - [Update Subcriber](#update-subcriber)
      - [Arguments](#arguments-11)
      - [Example](#example-11)
  - [Update Subscriber Service Plan](#update-subscriber-service-plan)
      - [Arguments](#arguments-12)
      - [Example](#example-12)
  - [Get Service Plans](#get-service-plans)
      - [Arguments](#arguments-13)
      - [Example](#example-13)
  - [Modify Service Plans](#modify-service-plans)
      - [Arguments](#arguments-14)
      - [Example](#example-14)

### Dependencies
Uses the [Requests](https://docs.python-requests.org/en/latest/) library for http.

```pip install requests```

## Basic Usage
Clone repository and copy boss.py into your project.

Then you can initiate the BOSS class by using
```python
from boss import BOSS

# CloudCore username and password
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

CLOUD_KEY = "" # Provided in your CloudCore instance

boss = BOSS(USERNAME, PASSWROD, CLOUD_KEY)
```

## Query Subscriber
Retrieve subscriber data from CloudCore.
### Query by ID
Query subscriber by subscriber ID.
#### Arguments
| Name  | Type   | Required |
|-------|--------|----------|
|sub_id | String | True     |

#### Example
```python
boss.query_by_id("sub_id")
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

### Query by IMSI
Query subscriber from IMSI number.
#### Arguments
| Name | Type |Required|
|------|------|--------|
|imsi  | Int  | True   |

#### Example
```python
boss.query_by_id("sub_id")
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Create Subscriber
Create new subscriber in CloudCore

### Create a Single Subscriber

#### Arguments
| Name | Type       | Required |
|------|------------|----------|
|sub   | Subscriber | True     |

#### Example
```python
from boss import Subscriber

new_sub = Subscriber(
    sub_id = "sub_id123",
    sub_name = "John Doe",
)

boss.create_sub(new_sub)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

### Bulk Create Subscribers

#### Arguments
| Name           | Type               | Required |
|----------------|--------------------|----------|
|service_plan_id | String             | True     |
|sub             | List of Subscriber | True     |

#### Example
```python
from boss import Subscriber

new_subs = [
    Subscriber(
        sub_id = "sub_id123",
        sub_name = "John Doe",
        imsi = 123451234512345
    ),
    Subscriber(
        sub_id = "sub_id123",
        sub_name = "Jim Bob",
        imsi = 123451234512346
    ),
    Subscriber(
        sub_id = "sub_id123",
        sub_name = "Jane Jones",
        imsi = 123451234512347
    )
]

boss.bulk_create_subs(
    service_plan_id = 'service123',
    subs = new_subs
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Bind Service Plan
Binds a service plan to a subscriber's account.
#### Arguments
| Name          | Type   | Required |
|---------------|--------|----------|
|service_plan_id| String | True     |
|sub_id         | String | False*   |
|imsi           | Int    | False*   |

*Must provide either sub_id or imsi

#### Example
```python
boss.bind_service_plan(
    "service123",
    imsi=123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Bind IMSI
Binds a SIM to a subscriber's account. Account must be deactivated and not have an IMSI already bound to it in order to bind.
#### Arguments
| Name          | Type   | Required |
|---------------|--------|----------|
|sub_id         | String | True     |
|imsi           | Int    | True     |


#### Example
```python
boss.bind_imsi(
    sub_id = "sub123",
    imsi = 123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Unbind IMSI
Unbind IMSI from subscriber's accounts. Requires account to be deactivated.

#### Arguments
| Name          | Type   | Required |
|---------------|--------|----------|
|sub_id         | String | False*   |
|imsi           | Int    | False*   |

*Must provide either sub_id or imsi

#### Example
```python
boss.unbind_imsi(
    imsi = 123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Activate Subscriber
Activates subscriber account. Requires service plan and IMSI to be bound to account.

### Activate Single Subscriber
#### Arguments
| Name          | Type   | Required |
|---------------|--------|----------|
|sub_id         | String | False*   |
|imsi           | Int    | False*   |

*Must provide either sub_id or imsi

#### Example
```python
boss.activate(
    imsi = 123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

### Bulk Activate Subscribers
#### Arguments
| Name          | Type            | Required |
|---------------|-----------------|----------|
|sub_id_list    | List of Strings | True     |

#### Example
```python
sub_ids = [
    'sub123', 'sub124', 'sub125'
]
boss.bulk_activate(
    sub_ids
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Deactivate Subscriber
Deactivates subscriber account.

### Deactivate Single Subscriber
#### Arguments
| Name          | Type   | Required |
|---------------|--------|----------|
|sub_id         | String | False*   |
|imsi           | Int    | False*   |

*Must provide either sub_id or imsi

#### Example
```python
boss.deactivate(
    imsi = 123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

### Bulk Deactivate Subscribers
#### Arguments
| Name          | Type            | Required |
|---------------|-----------------|----------|
|sub_id_list    | List of Strings | True     |

#### Example
```python
sub_ids = [
    'sub123', 'sub124', 'sub125'
]
boss.bulk_deactivate(
    sub_ids
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Update Subcriber
Update subscriber information.

#### Arguments
| Name | Type       | Required |
|------|------------|----------|
|sub   | Subscriber | True     |

#### Example
```python
from boss import Subscriber

updated_sub = Subscriber(
    imsi = 123451234512345,
    sub_name = "John Doe",
    phone_number = 5555551234
    email = "john.doe@example.com"
)

boss.update_sub(updated_sub)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Update Subscriber Service Plan
Change a specific subscriber's service plan.

#### Arguments
| Name           | Type   | Required |
|----------------|--------|----------|
|service_plan_id | String | True     |
|sub_id          | String | False*   |
|imsi            | Int    | False*   |

*Must provide either sub_id or imsi

#### Example
```python
boss.update_service_plan(
    "service124",
    imsi = 123451234512345
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Get Service Plans
Retrieve a list of all available service plans

#### Arguments
None

#### Example
```python
boss.get_service_plans()
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```

## Modify Service Plans
Modify a service plans speed and information

#### Arguments
| Name             | Type   | Required |
|------------------|--------|----------|
|service_plan_id   | String | True     |
|service_plan_name | String | False*   |
|uplink            | Int    | False*   |
|downlink          | Int    | False*   |

*Uplink and downlink are in MB/s
#### Example
```python
boss.modify_service_plan(
    service_plan_id = 'service123',
    service_plan_name = '10MB Plan',
    uplink = 10,
    downlink = 10
)
```

```python
# Returns
{
    "data": {...},
    "status_code": 200
}
```