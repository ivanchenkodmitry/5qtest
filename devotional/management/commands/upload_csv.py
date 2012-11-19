from devotional.models import Devotional
from django.core.management.base import BaseCommand, CommandError
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):

#        import pdb; pdb.set_trace()


        for file_name in args:
            try:

                csvfile = open(file_name)
                reader = list(csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True))
                for row in reader[1:]:

                    dev = Devotional.objects.create(title = row[0], month = int(row[1]), day = int(row[2]), body = row[3])
                    print 'Added devotional %s' % dev.title
            except:
                print 'Error: Invalid options or file'



