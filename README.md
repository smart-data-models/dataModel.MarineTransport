# dataModel.MarineTransport

### List of data models

The following entity types are available:
- [Berth](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Berth/README.md). This data model is intended to provide information about Berths. We define 'berth' to each stop of a ship during a PortCall, both for a port-facility (berth) and as an anchorage area. Each berth has a berthing time (estimated, planned, etc.), a lifecycle (estimated, requested, approved, etc.), an main activity during the stop (commercial operations, major repair, etc.) and a number of attributes described below. When commercial operations take place, an Operation entity will define the details of each commercial operation

- [Booking](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Booking/README.md). Provide the bookings electronic messaging description

- [EdiCodeco](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/EdiCodeco/README.md). A message by which a terminal, depot, etc. confirms that the containers specified have been delivered or picked up by the inland carrier (road, rail or barge). This message can also be used to report internal terminal container movements (excluding loading and discharging the vessel) and to report the change in status of container(s) without those containers having physically been moved. See [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)

- [Operation](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Operation/README.md). This data model is intended to provide information about commercial operations made in a stop of a ship during a PortCall (Berth entity). An Operation is defined as the activities related to commercial operations that take in place during the berth. Each Operation has an entity and some operations can be made in the same berth (docked or anchorage), and are distinguished by its sequence number on time (operationRank)

- [Port](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Port/README.md). The data model is intended to provide information about ports

- [PortAuthority](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortAuthority/README.md). The data model is intended to provide information about Port Authorities

- [PortCall](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortCall/README.md). This data model is intended to provide information about PortCalls (the visit of a ship to a port). It allows to represent the properties of each PortCall, including the visiting Vessel (partially loaded and referenced to Vessel entity for more info). On each attribute references related to elements of other well known standards are included. The data model is intended to provide the basic information about a PortCall, that is, the data relative to the arrival and the departure of the ship from the port, but not intermediate activities (berthing, operations, ...) that are defined in other linked entities (Berth, Operation, ...)

- [Vessel](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Vessel/README.md). The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information



### Contributors
[Link](https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/CONTRIBUTORS.yaml) to the 8 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.MarineTransport/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.MarineTransport/pulls) on existing data models
