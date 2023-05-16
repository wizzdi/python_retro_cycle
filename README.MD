retro_cycle.py deserializes Java's [Jackson Style references](https://fasterxml.github.io/jackson-annotations/javadoc/2.8/com/fasterxml/jackson/annotation/JsonIdentityReference.html%5D)

    @JsonIdentityInfo(generator =  ObjectIdGenerators.PropertyGenerator.class,  property  =  "json-id")
    @JsonIdentityReference(alwaysAsId =  true)  
    public  class  Customer{  
    private  String id;  
    private  String name;  
    private  Order order;  
    .............  }