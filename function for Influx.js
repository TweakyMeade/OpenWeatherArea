// script has multiple locations, this filters them into to messurements (Tables) 
//for influx2 and deletes it from the payload as it useless row. 
msg.measurement = msg.payload.Location;
delete msg.payload.Location
return msg;