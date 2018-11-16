conditions = [
  "and",
  [
    "or",
    [
      "or",
      {
        "type": "custom_attribute",
        "name": "browser",
        "value": "firefox"
      },
      {
        "type": "custom_attribute",
        "name": "browser",
        "value": "chrome"
      }

    ]
  ]
]

condition2 = [
  "and",
  [
    "or",
    [
      "or",
      {
        "type": "custom_attribute",
        "name": "browser",
        "value": "chrome"
      }
    ],
    [
      "or",
      {
        "type": "custom_attribute",
        "name": "color",
        "value": "red"
      }
    ]
  ]
]
