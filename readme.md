## Description
This adds a simple plugin for disabling wake word. 

In this case wake word is only triggered by button_press/bus signal


## Install

`pip install chatterbox-wake-word-plugin-dummy`

Then configure a wake_word with module to 'dummy_ww_plug`

NOTE: wakeword config is ignored and wake word name (or other fields) do not matter, you only need an entry with module set to "dummy_ww_plug"

```json
 "listener": {
      "wake_word": "dummy"
 },
 "hotwords": {
    "dummy": {
        "module": "dummy_ww_plug"
    }
  }
 
```

## Use cases

- linux phones or other low powered devices (cant run a full wake word engine)
- privacy critical applications (no listening unless physical action)
