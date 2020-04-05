# prodpad

This python module exists to make it easy to create python applications that interact with the [Prodpad API](https://help.prodpad.com/hc/en-us/sections/200724758-API-Documentation).

## Quick Start

To install, run `pip3 install prodpad`.

```python
	from prodpad install Prodpad
	
	prodpad = Prodpad(key)
	
	idea = prodpad.idea('1234')
	print(idea.title)


### Prerequisites

Runs on Python3 only.

### Installing

To install, run `pip3 install prodpad`.

## Running the tests

Coming soon...

## Contributing

Please read [contributions.md](https://gist.github.com/cmcgovern/6fc96f12935693f8930524a93a5c5c1c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Colin McGovern** - *Initial work* - [PurpleBooth](https://github.com/cmcgovern)

See also the list of [contributors](https://github.com/cmcgovern/prodpad/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


