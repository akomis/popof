import sys
import argparse
import csv

class Cost:
	bases = []

	def __init__(self, line):
		self.base = line[0]

		if self.base not in Cost.bases:
			Cost.bases.append(self.base)

		self.name = line[1]
		self.costs = line[2]
		self.period = line[3]

	def __str__(self):
		p = ''
		if self.period == 'd':
			p = 'Day'
		elif self.period == 'w':
			p = 'Week'
		else:
			p = 'Month'

		return "(" + self.base + ") " + self.name + "with cost: " + self.costs + " per " + p

	def getMonthlyCost(self):
		if self.period == 'd':
			return 30 * float(self.costs)
		elif self.period == 'w':
			return 4 * float(self.costs)
		else:
			return float(self.costs)


def validateRow(row, index):
	# If line is comment then ignore
	if row[0][0] == "#":
		return False

	# Check that there are no empty fields
	for field in row:
		if field == '':
			print("All fields must be filled.")
			return False

	# Check if price field is a positive number
	try:
		x = float(int(row[2]))

		if x < 0:
			raise ValueError()
	except:
		print("Costs field must contain a positive integer.")
		return False

	# Check if period field is valid (d, w or m)
	if row[3] not in ['d','w','m']:
		print(row[3])
		print("Row " + str(index) + " has invalid Period value (Can only be d/w/m)")
		return False

	return True

def positiveInt(value):
	ivalue = int(value)
	if ivalue < 0:
		raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)

	return ivalue

def goalMode(costs, savings):
	total = 0

	for base in costs:
		baseName = base[0].base
		for c in base:
			total += c.getMonthlyCost()
		print("To satisfy base up to " + baseName + " you need to make " + str(total+savings) + "\n")

def priorityMode(costs, income):
	budget = income

	for base in costs:
		baseName = base[0].base
		for c in base:
			if c.getMonthlyCost() <= budget:
				budget -= c.getMonthlyCost()
			else:
				print("Can't satisfy base " + baseName + " with " + c.name + " being the barrier")
				print("Base " + baseName + " could be satisfied if it had a " + str(budget) + " monthly cost\n")
				return

		print("Can satisfy base up to " + baseName + " with " + str(budget) + " in savings\n")

def main():
	parser = argparse.ArgumentParser(description="POPOF: Priority Oriented Perspective On Finances")
	parser.add_argument('-c', '--costs', type=str, help='Input csv file containing costs (check README for format)')
	parser.add_argument('-s', '--savings', type=positiveInt, help='Define goal for savings (Run GOAL mode)')
	parser.add_argument('-i', '--income', type=positiveInt, help='Define income (Run COVERAGE mode)')
	args = parser.parse_args()


	if args.costs is None:
		print("Please specify an input csv file containing costs as explained in the README")
		exit(1)

	validCosts = []
	with open(args.costs, 'r') as file:
		reader = csv.reader(file)

		i = 1
		for row in reader:
			# Remove leading and trailing spaces
			r = []
			for field in row:
				r.append(field.strip())

			if (validateRow(r, i)):
				validCosts.append(Cost(r))
			i += 1

	# Sort lines in costs
	costs = []
	for base in Cost.bases:
		temp = []
		for cost in validCosts:
			if cost.base == base:
				temp.append(cost)
		costs.append(temp)

	if args.savings is None and args.income is None:
		print("Please chose a mode of operation.")
		exit(2)

	if args.savings is not None:
		goalMode(costs, args.savings)

	if args.income is not None:
		priorityMode(costs, args.income)


if __name__ == "__main__":
	main()
