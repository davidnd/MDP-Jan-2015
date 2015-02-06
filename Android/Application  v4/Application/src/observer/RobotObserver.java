package observer;

public class RobotObserver {
	private static final RobotObserver robotObserver = new RobotObserver();
    
    private RobotObserver() {
         
    }
     
    public static RobotObserver getInstance() {
        return robotObserver;
    }
     
    public void register() {
         
    }
     
    public void noticeView() {
          
    }
}
