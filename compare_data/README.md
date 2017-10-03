# compare_gw

        HGS generate observation well output provides measurements like head, soil moisture, and elevation for 
        each simulation time step in block format. The purpose of this script is to post process the data into
        column format and perform transformation including:
		
		*convert head to depth
        *convert simulation time to real time
        *average data on weekly average
		
## Usage

            * read_raw_obs: read hgs observation well output (block format)

            * reorder_raw2column: convert bloc format to column format
            
            * head_to_depth: convert head to depth from surface elevation
            
            * to_realtime: convert simulation time (in seconds) to ISO time 

            * avg_weekly: averge all the columns on ISO calender week

            * op: output the processed data as CSV format

			
```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

