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
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
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
@Table(name = "django_admin_log")
//@NamedQueries({
//    @NamedQuery(name = "DjangoAdminLog.findAll", query = "SELECT d FROM DjangoAdminLog d")})
public class DjangoAdminLog implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "action_time")
    @Temporal(TemporalType.TIMESTAMP)
    private Date actionTime;
    @Column(name = "object_id")
    private String objectId;
    @Basic(optional = false)
    @Column(name = "object_repr")
    private String objectRepr;
    @Basic(optional = false)
    @Column(name = "action_flag")
    private short actionFlag;
    @Basic(optional = false)
    @Column(name = "change_message")
    private String changeMessage;
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    @ManyToOne(optional = false)
    private AuthUser userId;
    @JoinColumn(name = "content_type_id", referencedColumnName = "id")
    @ManyToOne
    private DjangoContentType contentTypeId;

    public DjangoAdminLog() {
    }

    public DjangoAdminLog(Integer id) {
        this.id = id;
    }

    public DjangoAdminLog(Integer id, Date actionTime, String objectRepr, short actionFlag, String changeMessage) {
        this.id = id;
        this.actionTime = actionTime;
        this.objectRepr = objectRepr;
        this.actionFlag = actionFlag;
        this.changeMessage = changeMessage;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Date getActionTime() {
        return actionTime;
    }

    public void setActionTime(Date actionTime) {
        this.actionTime = actionTime;
    }

    public String getObjectId() {
        return objectId;
    }

    public void setObjectId(String objectId) {
        this.objectId = objectId;
    }

    public String getObjectRepr() {
        return objectRepr;
    }

    public void setObjectRepr(String objectRepr) {
        this.objectRepr = objectRepr;
    }

    public short getActionFlag() {
        return actionFlag;
    }

    public void setActionFlag(short actionFlag) {
        this.actionFlag = actionFlag;
    }

    public String getChangeMessage() {
        return changeMessage;
    }

    public void setChangeMessage(String changeMessage) {
        this.changeMessage = changeMessage;
    }

    public AuthUser getUserId() {
        return userId;
    }

    public void setUserId(AuthUser userId) {
        this.userId = userId;
    }

    public DjangoContentType getContentTypeId() {
        return contentTypeId;
    }

    public void setContentTypeId(DjangoContentType contentTypeId) {
        this.contentTypeId = contentTypeId;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof DjangoAdminLog)) {
            return false;
        }
        DjangoAdminLog other = (DjangoAdminLog) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.DjangoAdminLog[ id=" + id + " ]";
    }
    
}
