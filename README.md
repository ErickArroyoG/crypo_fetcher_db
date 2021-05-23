# Crypto currency requester
To generate your own database of the price of cryptocurrencies.

## Response anatomy
Field Name  | Type    | Description                                       | Units
------------|---------|---------------------------------------------------|----------
book        | String  | Order book symbol                                 | Major\_Minor
volume      | String  | Last 24 hours volume                              | Major
high        | String	| Last 24 hours price high                          | Minor/Major
last        | String	| Last traded price                                 | Minor/Major
low         | String	| Last 24 hours price low                           | Minor/Major
vwap        | String	| Last 24 hours volume weighted average price: vwap | Minor/Major
ask         | String	| Lowest sell order                                 | Minor/Major
bid         | String	| Highest buy order                                 | Minor/Major
created\_at  | String	| Timestamp at which the ticker was generated       | ISO 8601 timestamp
