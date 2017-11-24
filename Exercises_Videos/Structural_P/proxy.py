"""Barbara Rodríguez López"""
"""GITI9071"""
"""Proxy Provide a substitute or representative of another object"""
import time

class Producer:
    """Define the 'resource-intensive' object to instantiate! """

    def produce(self):
        print("producer is working hard!")

    def meet(self):
        print("producer has time to meet you now")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as middleman """

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """check if producer is available """
        print("Artist checking if Producer is available  ")

        if self.occupied == 'No':
            # if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest
            self.producer.meet()

        else:
            # therwise, don't instantiate a producer
            time.sleep(2)
            print("producer is busy!")
            # Instantiate proxy
            p = Proxy()
            # Make the proxy: Artist produce until Producer is available
            p.produce()
            # Change the state to 'occupied'
            p.occupied = 'Yes'
            # Make the Producer produce
            p.produce()