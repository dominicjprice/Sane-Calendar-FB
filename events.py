import urllib2

f = urllib2.urlopen("[YOUR_EVENTS_URL]")
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
include = False
for line in f:
	if first:
		first = False
		buf += line
	if line.startswith("END:VCALENDAR"):
		break
	for line in f:
		if line.startswith("PARTSTAT"):
			if line.find("PARTSTAT:ACCEPTED") > -1 or line.find("PARTSTAT:TENTATIVE") > -1:
				include = True
			continue
		if line.find("CLASS:PRIVATE") > -1:
			line = line.replace("CLASS:PRIVATE", "CLASS:PUBLIC")
		if line.startswith("SEQUENCE"):
			line = line.strip()
			line += "0\r\n"
		buf += line.replace("\\:", " - ")
		if line.startswith("END:VEVENT"):
			break
	if include:
		print buf,
	buf = "BEGIN:VEVENT\r\n"
	include = False
print "END:VCALENDAR\r\n",
	
f.close()
