public class Memory extends Product{
    private String frequency;
    private Integer memorySize;
    private Boolean supportCuda;

    public Memory(){}

    public Memory(String frequency, Integer memorySize, Boolean supportCuda){
        this.frequency = frequency;
        this.memorySize = memorySize;
        this.supportCuda = supportCuda;
    }

    public void setFrequency(String frequency)
    {
        this.frequency = frequency;
    }

    public String getFrequency()
    {
        return this.frequency;
    }

    public void setMemorySize(Integer memorySize)
    {
        this.memorySize = memorySize;
    }

    public Integer getMemorySize()
    {
        return this.memorySize;
    }

    public void setSupportCuda(Boolean supportCuda)
    {
        this.supportCuda = supportCuda;
    }

    public Boolean getSupportCuda()
    {
        return this.supportCuda;
    }
}