def how_many_seconds(hours):
	seconds=hours*60*60
	return(seconds)

hours=int(input("Enter no.of hours"))
hours_to_seconds=how_many_seconds(hours)
print("No.of seconds is",hours_to_seconds)