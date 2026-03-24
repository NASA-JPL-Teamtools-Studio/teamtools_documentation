# Dante
Derivation Assistant for Novel Telemetry Expression

![Project logo](https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/raw/main/docs/images/tts_image_artifacts/dante.png)

### Overview

Dante is the TTS answer to when a system that produces data doesn't produce the data that you want. The most typical need for Dante at JPL
is creating ground derived channels if those are not yet available in your project's GDS for any reason.

For those outside of JPL, a primer... AMPCS is the software used to connect with the DSN, decomm telemetry, and turn it into time
series data. AMPCS has a notion of "ground derived channels" (think dn to eu conversion as a simple example). AMPCS can combine
data from the spacecraft to make new channels that the spacecraft has no knowledge of, and Dante serves a very similar funciton.

This is not meant to be a replacement for AMPCS Ground Derived Channels, but as an admission that the AMPCS GDC infrastructure 
has its pros as well as cons. Pseudo-channels in this library will NEVER flow back into legacy CHILL databases, but may be 
put into tools like EAS's State Data Store for query later. 

Reasons you'd want to have Dante:

* GDS budgets and schedules are such that your Java-derived channel is not ready and you need something like it NOW
* You want to derive a channel in a way that is not possible or is prohibitively hard in the AMPCS Java layer (e.g. using data products in a complex way)
* You have a complex enough channel that you find it more tractible to just have your team do it rather than have to communicate from your team to GDS to your team.

Reasons you'd want to use AMPCS instead:

* Bit-derived channels. Unless using Dante as a workaround, DON'T put bit derived channels here as that subverts many assumptions about how those should work.
* Channels that you need to see in Chill/Chillax queries. There is some chance that SysQuery could help us here, but that's work to go with a lot of moving parts, so don't count on it.
* If you believe that the formal V&V that is inherent in the AMPCS GDC process is valuable. Keep in mind that any channels derived with Dante will be done at the TEAMTOOL layer. That implies more flexibility, but also more risk.


### Projects Currently Supported

* NISAR Prototype

## Architecture

### TTS dependencies

* TTS Utilities
* TTS Data Utils

---
**Repository Links:** <a href="nasa-jpl-teamtools-studio.github.io/NASA-JPL-Teamtools-Studio/tts_dante/" target="_blank" rel="noopener noreferrer">Docs</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_dante/issues" target="_blank" rel="noopener noreferrer">Issues</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_dante" target="_blank" rel="noopener noreferrer">Source</a>