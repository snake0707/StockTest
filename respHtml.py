#---------------------------------import---------------------------------------
import urllib2;

#------------------------------------------------------------------------------
def main():
    userMainUrl = "http://www.google.com/finance/getprices?q=000001&x=SHA&i=86400&p=6M&f=d,c,v,o,h,l";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    print "respHtml=",respHtml; # you should see the ouput html

###############################################################################
if __name__=="__main__":
    main();