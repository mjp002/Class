package JC;

public class TV {
    int channel;

    public TV() {}

    public TV(int intValue) {
        this.channel = intValue;
    }

    protected void channelUp() {
        channel = channel + 1;

    }
    //메소드의 접근 제한자를 protected 로 변경
    private void channelDown() {
        channel = channel - 1;
        if (channel <0){
            channel = 0;
        }
    }
}
