
 
def process(params):
    switch = {
              "Table of Contents" : "This teacher guide consists of four segments - Introduction,Eight Lessons, Pausing Point and Domain Review.Which segment would you like to hear?",
              "Edition" : "2017"
            }
    response = switch[params["miscellaneous"]]
    return response       