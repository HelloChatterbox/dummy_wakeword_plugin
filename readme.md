## Description
This adds a simple plugin for disabling wake word. In this case mycroft will only answer by button_press/bus signal

The "plugins" are pip install-able modules presenting one or more entrypoints with a entrypoint group defined in setup.py

Wake-word group: "mycroft.plugin.wake_word"

more info in the [original PR](https://github.com/MycroftAI/mycroft-core/pull/2594)

## How to test

`mycroft-pip install git+https://github.com/HelloChatterbox/dummy_wakeword_plugin`

Then set the wake_word module to 'dummy_ww_plug` assert that mycroft does not answer to wake word

## Use cases

- linux phones or other low powered devices (cant run precise)
- privacy critical applications (no listening unless physical action)
