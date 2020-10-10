# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from mycroft.client.speech.hotword_factory import HotWordEngine


class DummyWakeWordPlugin(HotWordEngine):
    """Dummy Wake Word, only button presses trigger listening"""
    def __init__(self, hotword="dummy", config=None, lang="en-us"):
        super(DummyWakeWordPlugin, self).__init__(hotword, config or {}, lang)

    def found_wake_word(self, frame_data):
        return False

    def update(self, chunk):
        pass

    def stop(self):
        """ Perform any actions needed to shut down the hot word engine.

            This may include things such as unload loaded data or shutdown
            external processess.
        """
        pass
