# Solar Thermal Collector Mk1 General Notes Page

### Other Associated Pages

[Solar Thermal Collector Mk1 Experiment 1](solar_therm_mk1_experiment1.html)

### Objective

The goal of this project is to get me started with building actual energy
collection devices. Ideally this project should take the water source and
achieve elevated temperatures.

### Assumptions/Design

A simple design was decided upon for my first solar thermal project. A hot
water pump will take water from a source (bucket) and pump it through rubber
tubing that goes through empty/cleaned 2L bottles and deposit the water back in
the source. 

After deciding on using 8 2L bottles the length was determined to be around 30
feet. This allows ~2 feet per bottle, a foot between each bottle and ~2-3 feet
between the bottle array and the water source (bucket)

<div align="center">
<table class="image">
<caption align="bottom">Top View of Whole System</caption>
<tr><td><img src="./img/top_view.svg"
alt="Top View of Whole System" title="Top View of Whole System"/>
</td></tr>
</table>
</div>

### Parts list/Budget

<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
}
</style>
<div align="center">
<table>

  <tr>
  <th> Item </th>
  <th> Cost </th>		
  </tr>

  <tr>
  <td style="text-align:left"> <a href="http://www.amazon.com/Thermometers-Habor-Thermometer-Anti-Corrosion-Best/dp/B0198473E4/ref=sr_1_4?ie=UTF8&qid=1459874105&sr=8-4&keywords=water+thermometer" target="_blank">Temperature Sensor</a> </td>
  <td style="text-align:center"> $6.99 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> <a href="http://www.amazon.com/Hydrofarm-HG5G-5-Gallon-Black-Bucket/dp/B000VBW17S/ref=sr_1_3?ie=UTF8&qid=1459874474&sr=8-3&keywords=5+gallon+bucket" target="_blank">5 Gallon Bucket</a> </td>
  <td style="text-align:center"> $9.95 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> <a href="http://www.amazon.com/bayite-BYT-7A006-Solar-Water-Circulation/dp/B0196WL55G/ref=sr_1_1?ie=UTF8&qid=1459874765&sr=8-1&keywords=solar+hot+water+pump" target="_blank">Hot Water Pump</a> </td>
  <td style="text-align:center"> $21.98 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> <a href="http://www.amazon.com/Feet-Black-Rubber-Latex-Tubing/dp/B004HEAFSW/ref=pd_sim_200_11?ie=UTF8&dpID=41APAj37U-L&dpSrc=sims&preST=_AC_UL160_SR160%2C160_&refRID=0AC37MJMZ416N3BQ34CK" target="_blank">Plastic/Rubber Tubing</a> </td>
  <td style="text-align:center"> $31.39 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> <a href="http://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-48-Pack/dp/B00MNV8E0C/ref=sr_1_1_a_it?ie=UTF8&qid=1460245484&sr=8-1&keywords=aa+batterys+amazon+48+pack" target="_blank">48 Count AA Batteries</a> </td>
  <td style="text-align:center"> $12.09 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> 8 Recycled 2L Bottles </td>
  <td style="text-align:center"> $--.-- </td>		
  </tr>

  <tr>
  <td style="text-align:left"> Total Cost </td>
  <td style="text-align:center"> $82.40 </td>		
  </tr>

</table>
</div>

> __Parts Research__

>> __Temperature Sensor__

>> - There are different thermometers available that could meet this purpose
>>      - Fish tank thermometer
>>      - Cooking/grilling thermometer
>> - Going with a grilling thermometer because it will probably be better
     suited for elevated temperatures that I plan to achieve with the thermal
     collector system

>> __Hot Water Pump__

>> - Looking at 12V water pumps because they're smaller and more economical
>> - Going to need to find a way to power the pump
>> - It is unclear what size the included brass couplers are

>> __Rubber Tubing__

>> - Guessing I'll need 30 feet (see assumptions/design)
>>      - Lots of tubing only available in 10ft, 25ft, 50ft lengths
>> - Decided on a 1/4th in inner diameter tube with 20 extra feet just in case
>>      - Hopefully the tube will stretch over the hot water pump opening
>>      - Would be cheaper to buy new brass couplers instead of new tubing if
          it doesn't fit

>> __Power Supply__

>> - Decided it'd be cheapest to just use the 8 AA battery holder to supply the
     12 volts required by the heat pump
>> - Might long run end up being more expensive if the batteries do not last
     for long periods of time

### Implementation

> __The hose doesnt fit the brass couplers that came with the pump__

> - The hose did not end up fitting the couplers that came with the hot water
    pump and so a method of attaching them had to be determined
> - I was able to get a 1/2" to 1/4" adapter + 1/4" to 1/4" brass coupler to
    work to attach the hose to the pump
>       - This was ~$18 for two adapter/coupler sets
> - Future Considerations:
>       - Should try to find a hose with a larger inner diameter to fit the
          couplers that came with the pump
>       - Other option would be to find a pump that comes with a smaller
          diameter coupler to begin with

> __Putting holes in the bottle caps__

> - Initially tried scissors but that turned out to be infeasible
> - Borrowed a drill from a friend that that seems to be doing the trick really
    well
>       - Bought a drill bit set for ~$13
>       - Using a 1/8" bit to make the guide hole and a 3/8" bit to drill the
          actual hole
>           - Hose fits well in this hole

> __First Run__

> - The tubing ended up being two ~25 ft (I'm guessing they were about equal in
    length) tubes instead of one 50 ft tube
>       - Only able to fit 6 bottles instead of 8
> - The pump worked properly and was able to move the water all the way through
    the tube
> - There appeared to be no leaks in the system
> - I did not account for the space that the bottle would occupy inside the
    bottle caps and thus the tubing may have been slightly pinched in the
    opening for the cap
> - The temperature of the water did increase over the course of the hour but I
    do not know to what extent it was from the solar thermal collector or if it
    was just heating up to ambient temperature from whatever temperature the
    pipes were underground

>> __Temp change chart__

<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
}
</style>
<div align="center">
<table>

  <tr>
  <th> Time (min) </th>
  <th> Temperature (deg C) </th>		
  </tr>

  <tr>
  <td style="text-align:left"> ~0 </td>
  <td style="text-align:center"> 25.8 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> ~15 </td>
  <td style="text-align:center"> 28.2 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> ~30 </td>
  <td style="text-align:center"> 29.8 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> ~45 </td>
  <td style="text-align:center"> 31.2 </td>		
  </tr>

  <tr>
  <td style="text-align:left"> ~60 </td>
  <td style="text-align:center"> 32.5 </td>		
  </tr>

</table>
</div>

>> __Photos__

<div align="center">
<table class="image">
<tr><td><img src="./img/bucketarray_2.jpg"
alt="Bucket Array" title="Bucket Array" height="400" width="600"/>
</td></tr>
</table>
</div>

<div align="center">
<table class="image">
<tr><td><img src="./img/bottlearray.jpg"
alt="Bottle Array" title="Bottle Array" height="400" width="600"/>
</td></tr>
</table>
</div>

<div align="center">
<table class="image">
<tr><td><img src="./img/bottle_closeup.jpg"
alt="Bottle Close Up" title="Bottle Close Up" height="400" width="600"/>
</td></tr>
</table>
</div>

<div align="center">
<table class="image">
<tr><td><img src="./img/hot_water_pump.jpg"
alt="Hot Water Pump" title="Hot Water Pump" height="400" width="600"/>
</td></tr>
</table>
</div>

<div align="center">
<table class="image">
<tr><td><img src="./img/battery_pic.jpg"
alt="Battery Pic" title="Battery Pic" height="400" width="600"/>
</td></tr>
</table>
</div>

> __Ideas for Improvement__

> - Add foil under the bottles
> - Get a lid for the 5 gal bucket
> - Automate the temperature collection process
> - Insulate the bucket
> - Use a splitter for the tubing so that both 25 ft segments can be used
> - Wrap electrical tape or some equivalent around the tubing at the bottle
    caps to better insulate the bottles
> - Run the pump off of a rechargable battery and use a solar panel to charge
    the battery
