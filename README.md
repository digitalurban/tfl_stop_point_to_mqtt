# tfl_stop_point_to_mqtt

Gets the next 5 bus or tube arrivals and publishes to mqtt

Uses the TFL api to fecth the latest 5 bus or tube arrivals and publish to mqtt - edit the stop point code as needs be.

The example is Goodge Street, Heading North.

The python script sorts and tidies the output for a printable list.

It is designed to be run as a cron task - every set number of minutes to push the data to an mqtt topic for display.



