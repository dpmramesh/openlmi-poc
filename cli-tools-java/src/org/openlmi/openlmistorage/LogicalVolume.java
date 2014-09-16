package org.openlmi.openlmistorage;

public class LogicalVolume {

    private String name;
    private String blockSize;
    private String NoOfBlocks;

    public LogicalVolume(String name, String blockSize, String noOfBlocks) {
        super();
        this.name = name;
        this.blockSize = blockSize;
        NoOfBlocks = noOfBlocks;
    }

    public String getName() {
        return name;
    }

    public String getBlockSize() {
        return blockSize;
    }

    public String getNoOfBlocks() {
        return NoOfBlocks;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setBlockSize(String blockSize) {
        this.blockSize = blockSize;
    }

    public void setNoOfBlocks(String noOfBlocks) {
        NoOfBlocks = noOfBlocks;
    }

}
