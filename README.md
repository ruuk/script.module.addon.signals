[![GitHub release](https://img.shields.io/github/release/ruuk/script.module.addon.signals.svg)](https://github.com/ruuk/script.module.addon.signals/releases)
[![Build Status](https://travis-ci.org/ruuk/script.module.addon.signals.svg?branch=master)](https://travis-ci.org/ruuk/script.module.addon.signals)
[![License: LGPL-2.1](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/LGPL-2.1-only)
[![Contributors](https://img.shields.io/github/contributors/ruuk/script.module.addon.signals.svg)](https://github.com/ruuk/script.module.addon.signals/graphs/contributors)

# script.module.addon.signals
Provides signal/slot mechanism for inter-addon communication in Kodi

```python
# In target addon
import AddonSignals
​
def callback(data):
	# Do something with data
	
AddonSignals.registerSlot('sender.addon.id', 'signal_name', callback)
​
​
#In source addon
import AddonSignals
​
AddonSignals.sendSignal('signal_name', {'some': 'data'})
```
