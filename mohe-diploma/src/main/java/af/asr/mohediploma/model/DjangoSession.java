/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.Date;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "django_session")
//@NamedQueries({
//    @NamedQuery(name = "DjangoSession.findAll", query = "SELECT d FROM DjangoSession d")})
public class DjangoSession implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @Column(name = "session_key")
    private String sessionKey;
    @Basic(optional = false)
    @Column(name = "session_data")
    private String sessionData;
    @Basic(optional = false)
    @Column(name = "expire_date")
    @Temporal(TemporalType.TIMESTAMP)
    private Date expireDate;

    public DjangoSession() {
    }

    public DjangoSession(String sessionKey) {
        this.sessionKey = sessionKey;
    }

    public DjangoSession(String sessionKey, String sessionData, Date expireDate) {
        this.sessionKey = sessionKey;
        this.sessionData = sessionData;
        this.expireDate = expireDate;
    }

    public String getSessionKey() {
        return sessionKey;
    }

    public void setSessionKey(String sessionKey) {
        this.sessionKey = sessionKey;
    }

    public String getSessionData() {
        return sessionData;
    }

    public void setSessionData(String sessionData) {
        this.sessionData = sessionData;
    }

    public Date getExpireDate() {
        return expireDate;
    }

    public void setExpireDate(Date expireDate) {
        this.expireDate = expireDate;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (sessionKey != null ? sessionKey.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof DjangoSession)) {
            return false;
        }
        DjangoSession other = (DjangoSession) object;
        if ((this.sessionKey == null && other.sessionKey != null) || (this.sessionKey != null && !this.sessionKey.equals(other.sessionKey))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.DjangoSession[ sessionKey=" + sessionKey + " ]";
    }
    
}
