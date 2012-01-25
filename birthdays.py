import urllib2

f = urllib2.urlopen("[YOUR_BIRTHDAYS_URL]")
for line in f:
	if line.startswith("BEGIN:VCALENDAR"):
		break
print 'Content-Type: text/calendar'
print ''
print "BEGIN:VCALENDAR\r\n",
for line in f:
	if not line.startswith("BEGIN:VEVENT"):
		print line,
	else:
		break
buf = "BEGIN:VEVENT\r\n"
first = True
for line in f:
	if first:
		first = False
		if line.startswith("DTSTART"):
                        line = line.strip()
                        line += "T000000Z\r\n"
		buf += line
	if line.startswith("END:VCALENDAR"):
		break
	for line in f:
		if line.startswith("PARTSTAT"):
			continue
		if line.find("CLASS:PRIVATE") > -1:
			line = line.replace("CLASS:PRIVATE", "CLASS:PUBLIC")
		if line.startswith("DTSTART"):
			line = line.strip()
			line += "T000000Z\r\n"
		if line.startswith("SEQUENCE"):
			line = line.strip()
			line += "0\r\n"
		buf += line.replace("\\:", " - ")
		if line.startswith("END:VEVENT"):
			break
	print buf,
	buf = "BEGIN:VEVENT\r\n"
print "END:VCALENDAR\r\n",
	
f.close()
