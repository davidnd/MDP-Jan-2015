package observer;

public class ArenaObserver {
	private static final ArenaObserver arenaObserver = new ArenaObserver();
    
    private ArenaObserver() {
         
    }
     
    public static ArenaObserver getInstance() {
        return arenaObserver;
    }
     
    public void register() {
         
    }
     
    public void noticeView() {
        //Drawer.getInstance().update();
    }
}
