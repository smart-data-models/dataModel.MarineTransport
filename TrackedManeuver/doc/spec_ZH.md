<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：TrackedManeuver  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**TrackedManoeuvre 实体来自 Tracked（操作跟踪系统）。跟踪机动。实体 ID 按照模式 mrn:urn:eshuv:pdph:Tracked:type:attr:value 进行命名，其中 type=Manoeuvre 且 attr=manoeuvreCode**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，那是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且在该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：地区所在的国家。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：一个区是一个类型的行政区划，在一些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱编号。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：在公共街道上标识特定属性的编号    
- `alternateName[string]`：该项的另一个名称  - `amendedOnMooringLocation[string]`：“固定在旁边/修改停泊”机动的位置  - `anchoringAnchorUpDate[date-time]`：锚起（锚上）时间，用于锚泊机动  - `anchoringDate[date-time]`：锚下时间，用于锚泊机动  - `anchoringLocation[*]`：Geojson 引用项。可以是点、线串、多边形、多点、多线串或多多边形  - `anchoringZone[string]`：锚泊机动的锚区  - `areaServed[string]`：服务或提供项提供的地域。模型：[https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`：一个字符序列，标识和谐数据实体的提供者  - `dateCreated[date-time]`：实体创建时间戳。这通常由存储平台分配  - `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配  - `description[string]`：该项的描述  - `durationHours[number]`：机动持续时间（小时）  - `endDate[date-time]`：机动结束日期  - `id[*]`：实体的唯一标识符  - `location[*]`：Geojson 引用项。可以是点、线串、多边形、多点、多线串或多多边形  - `maneuverCode[string]`：机动代码  - `maneuverType[string]`：机动类型  - `mooringCablesNumber[number]`：停泊机动的线数  - `mooringChangeCablesNumber[number]`：泊位转移机动的线数  - `mooringChangeFirstLandCableDate[date-time]`：泊位转移机动的第一条线时间  - `mooringChangeInitialLocation[string]`：泊位转移机动的初始位置  - `mooringChangeLastCableDate[date-time]`：泊位转移机动的最后一条线时间  - `mooringChangeLastLocation[string]`：泊位转移机动的最终位置  - `mooringChangeNoraysFrom[number]`：泊位转移机动的起始系泊点编号  - `mooringChangeNoraysTo[number]`：泊位转移机动的结束系泊点编号  - `mooringChangeSide[string]`：泊位转移机动的系泊侧  - `mooringFirstCableDate[date-time]`：停泊机动的第一条线时间  - `mooringLocation[string]`：停泊机动的位置  - `mooringNoraysFrom[number]`：停泊机动的起始系泊点编号  - `mooringNoraysTo[number]`：停泊机动的结束系泊点编号  - `mooringSide[string]`：停泊机动的系泊侧  - `name[string]`：该项的名称  - `observations[string]`：机动观察  - `observedDate[date-time]`：实体的最后更新日期  - `othersLocation[*]`：Geojson 引用项。可以是点、线串、多边形、多点、多线串或多多边形  - `othersType[string]`：其他机动的类型  - `othersZone[string]`：其他机动的区域/位置  - `owner[array]`：一个包含 JSON 编码序列的列表，引用所有者（们）的唯一 ID  - `pilotageDisembarkDate[date-time]`：引水员下船时间，用于引水机动  - `pilotageDisembarkLocation[string]`：引水员下船位置，用于引水机动  - `pilotageEmbarkDate[date-time]`：引水员上船时间，用于引水机动  - `pilotageEmbarkLocation[string]`：引水员上船位置，用于引水机动  - `pilotageExempt[string]`：引水豁免  - `pilotageObservations[string]`：引水机动观察  - `pilotagePilots[string]`：参与引水机动的引水员  - `portCallCode[string]`：港口呼叫的 STM 注册表  - `refPortCallId[string]`：对港口呼叫的引用  - `refTugServiceId[string]`：对拖船服务的引用  - `seeAlso[*]`：关于该项的其他资源的 URI 列表  - `source[string]`：一个字符序列，给出实体数据的原始来源作为 URL。建议为源提供者的全限定域名，或源对象的 URL  - `startDate[date-time]`：机动开始日期  - `tugboatsNumber[number]`：拖船服务机动的拖船数量  - `tugboatsObservations[string]`：拖船服务机动观察  - `type[string]`：NGSI 实体类型。必须是 TrackedManoeuvre  - `undockingLastCableDate[date-time]`：解泊（撤离）机动的最后一条线时间  - `undockingLocation[string]`：解泊（撤离）机动的位置  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（点击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的 YAML 详细信息</strong></summary>    
```yaml  
TrackedManeuver:    
  description: TrackedManoeuvre entity coming from Tracked (Operation Tracking System). Tracked maneuver. The entityId follows the pattern mrn:urn:eshuv:pdph:Tracked:type:attr:value, where type=Manoeuvre and attr=manoeuvreCode    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    amendedOnMooringLocation:    
      description: Location of the 'made fast alongside / amended on mooring' maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringAnchorUpDate:    
      description: Anchor aweigh (anchor up) time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringDate:    
      description: Anchor down time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    anchoringZone:    
      description: Anchorage zone for the anchoring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    durationHours:    
      description: Maneuver duration in hours    
      type: number    
      x-ngsi:    
        type: Property    
    endDate:    
      description: Maneuver end date    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    maneuverCode:    
      description: Maneuver code    
      type: string    
      x-ngsi:    
        type: Property    
    maneuverType:    
      description: Maneuver type    
      type: string    
      x-ngsi:    
        type: Property    
    mooringCablesNumber:    
      description: Number of lines for the mooring maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeCablesNumber:    
      description: Number of lines for the berth-shifting maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeFirstLandCableDate:    
      description: First shore line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeInitialLocation:    
      description: Initial location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastCableDate:    
      description: Last line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastLocation:    
      description: Final location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysFrom:    
      description: Bollard number from (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysTo:    
      description: Bollard number to (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeSide:    
      description: Mooring side for the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringFirstCableDate:    
      description: First line time for the mooring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringLocation:    
      description: Location of the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringNoraysFrom:    
      description: Bollard number from (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringNoraysTo:    
      description: Bollard number to (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringSide:    
      description: Mooring side for the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observations:    
      description: Maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    observedDate:    
      description: Last update date of the entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    othersLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    othersType:    
      description: Type of other maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    othersZone:    
      description: Zone/location of the other maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    pilotageDisembarkDate:    
      description: Pilot disembarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageDisembarkLocation:    
      description: Pilot disembarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkDate:    
      description: Pilot embarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkLocation:    
      description: Pilot embarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageExempt:    
      description: Pilotage exemption    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageObservations:    
      description: Pilotage maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    pilotagePilots:    
      description: Pilots involved in the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    portCallCode:    
      description: STM register of the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refPortCallId:    
      description: Reference to the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refTugServiceId:    
      description: Reference to the tug service    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    startDate:    
      description: Maneuver start date    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    tugboatsNumber:    
      description: Number of tugboats for the tug service maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    tugboatsObservations:    
      description: Tug service maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TrackedManoeuvre    
      enum:    
        - TrackedManeuver    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLastCableDate:    
      description: Last line time for the unmooring (undocking) maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLocation:    
      description: Location of the unmooring (undocking) maneuver    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/TrackedManoeuvre/schema.json    
  x-model-tags: ESHUV, i4trust, Tracked    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 示例有效载荷    
#### TrackedManeuver NGSI-v2 键值示例    
这是一个 TrackedManeuver 的 JSON 格式示例，作为键值。它与 NGSI-v2 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque"  
}  
```  
</details>  
#### TrackedManeuver NGSI-v2 标准示例    
这是一个 TrackedManeuver 的 JSON 格式示例，作为标准。它与 NGSI-v2 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "refPortCallId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Text",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Text",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Text",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "durationHours": {  
    "type": "Number",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Text",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringLocation": {  
    "type": "Text",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Number",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Number",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Text",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeLastLocation": {  
    "type": "Text",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Number",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Text",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "undockingLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "anchoringAnchorUpDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "othersType": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotagePilots": {  
    "type": "Text",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Text",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Text",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Number",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Text",  
    "value": "Observaciones de remolque"  
  }  
}  
```  
</details>  
#### TrackedManeuver NGSI-LD 键值示例    
这是一个 TrackedManeuver 的 JSON-LD 格式示例，作为键值。它与 NGSI-LD 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TrackedManeuver NGSI-LD 标准示例    
这是一个 TrackedManeuver 的 JSON-LD 格式示例，作为标准。它与 NGSI-LD 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "refPortCallId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Property",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Property",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Property",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "durationHours": {  
    "type": "Property",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Property",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringLocation": {  
    "type": "Property",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Property",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Property",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Property",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeLastLocation": {  
    "type": "Property",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Property",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Property",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "undockingLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "anchoringAnchorUpDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "othersType": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotagePilots": {  
    "type": "Property",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Property",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Property",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Property",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Property",  
    "value": "Observaciones de remolque"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以获取有关如何处理数量单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->