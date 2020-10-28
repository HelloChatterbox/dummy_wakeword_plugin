## Description
This adds a simple plugin for disabling wake word. In this case mycroft will only answer by button_press/bus signal

The "plugins" are pip install-able modules presenting one or more entrypoints with a entrypoint group defined in setup.py

Wake-word group: "mycroft.plugin.wake_word"

more info in the [original PR](https://github.com/MycroftAI/mycroft-core/pull/2594)


## How to test

`mycroft-pip install git+https://github.com/HelloChatterbox/dummy_wakeword_plugin`

Then configure a wake_word with module to 'dummy_ww_plug`, assert that mycroft does not answer to wake word

NOTE: wakeword config is ignored and wake word name (or other fields) do not matter, you only need an entry with module set to "dummy_ww_plug"

## Use cases

- linux phones or other low powered devices (cant run precise)
- privacy critical applications (no listening unless physical action)
