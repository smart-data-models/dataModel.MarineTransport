/* (Beta) Export of data model Company of the subject dataModel.MarineTransport 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE entityType_type AS ENUM ('Agent', 'Carrier', 'Consignee', 'LogisticsOperator', 'PortAuthority', 'PortReceptionFacilityOperator', 'PublicBody', 'ServiceProvider', 'Steevedore', 'TerminalOperator', 'TransportCompany', 'WasteManagementCompany', 'Other');

CREATE TABLE Company (
    active BOOLEAN,
    address JSON,
    admissionDate TEXT,
    alias TEXT,
    alternateName TEXT,
    areaServed TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    description TEXT,
    email TEXT,
    entityType entityType_type,
    id TEXT PRIMARY KEY,
    legalCode TEXT,
    licenses JSON,
    location JSON,
    mrn TEXT,
    name TEXT,
    owner JSON,
    registeredName TEXT,
    seeAlso JSON,
    source TEXT,
    telephone TEXT
);