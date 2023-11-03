
def count_batteries_by_health(present_capacities):
  healthy_count = 0
  exchange_count = 0
  failed_count = 0

for capacity in present_capacitens:
  #calculate self for each battery
  rated_capacity = 120 
  soh = (capacity / rated_capacity) * 100

#classify the battery based on self
if soh > 80:
   healthy +=1
elif 62 <= soh <= 80:
  exchange +=1
else:
  failed =+1
  
#Return the counts
return {
  "healthy" : healthy_count,
  "exchange" : exchange_count,
  "failed" : failed_count
}
  

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [20,85,50,90,110,120,100,30,49,119,102,99]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 4)
  assert(counts["failed"] == 5)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
