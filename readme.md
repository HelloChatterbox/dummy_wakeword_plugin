## Description
This adds a simple plugin for disabling wake word. In this case mycroft will only answer by button_press/bus signal

The "plugins" are pip install-able modules that provide new engines for mycroft

more info in the [docs](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins)

## Install

`mycroft-pip install chatterbox-wake-word-plugin-dummy`

Then configure a wake_word with module to 'dummy_ww_plug`, assert that mycroft does not answer to wake word

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

- linux phones or other low powered devices (cant run precise)
- privacy critical applications (no listening unless physical action)
