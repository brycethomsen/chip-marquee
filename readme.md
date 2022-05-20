# Marquee UI for BetaBrite signs

Python app that writes text to Betabrite signs. 

* Marquee-ui is a flask UI that allows users enter messages to display on the sign
* UI allows users to set the message, color, font and mode
* Mode is simply how the text will be displayed
* The UI writes everything to a sqlite database
* Marquee-updater reads from the database and sends the commands to the sign
* Both apps can run as a systemd service with the service files
* Both apps can also run within docker using the Dockerfile and docker-compose-yml files

Big thanks to https://github.com/brycethomsen/chip-marquee for starting this whole thing! 