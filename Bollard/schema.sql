/* (Beta) Export of data model Bollard of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE mrn_type AS ENUM ('PortCall');
CREATE TYPE Bollard_type AS ENUM ('Bollard');

CREATE TABLE Bollard (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    bollardIndex NUMERIC,
    code TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    description TEXT,
    distanceFromPrevious NUMERIC,
    distanceFromStart NUMERIC,
    facilityRef TEXT,
    id TEXT PRIMARY KEY,
    latitude NUMERIC,
    location JSON,
    longitude NUMERIC,
    modifiedDate TIMESTAMP,
    mrn mrn_type,
    name TEXT,
    outOfOrder BOOLEAN,
    owner JSON,
    portCode TEXT,
    probe NUMERIC,
    seeAlso JSON,
    source TEXT,
    type Bollard_type
);