/* (Beta) Export of data model NavigationSector of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE mrn_type AS ENUM ('PortCall');
CREATE TYPE NavigationSector_type AS ENUM ('NavigationSector');

CREATE TABLE NavigationSector (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    description TEXT,
    id TEXT PRIMARY KEY,
    location JSON,
    minProbe NUMERIC,
    minProbeDate TIMESTAMP,
    modifiedDate TIMESTAMP,
    mrn mrn_type,
    name TEXT,
    navigationArea TEXT,
    navigationSector TEXT,
    owner JSON,
    portCode TEXT,
    rank NUMERIC,
    remarks TEXT,
    sectorType TEXT,
    seeAlso JSON,
    source TEXT,
    type NavigationSector_type
);