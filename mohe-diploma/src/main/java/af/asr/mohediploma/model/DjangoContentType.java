/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "django_content_type")
//@NamedQueries({
//    @NamedQuery(name = "DjangoContentType.findAll", query = "SELECT d FROM DjangoContentType d")})
public class DjangoContentType implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "app_label")
    private String appLabel;
    @Basic(optional = false)
    @Column(name = "model")
    private String model;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "contentTypeId")
    private List<AuthPermission> authPermissionList;
    @OneToMany(mappedBy = "contentTypeId")
    private List<DjangoAdminLog> djangoAdminLogList;

    public DjangoContentType() {
    }

    public DjangoContentType(Integer id) {
        this.id = id;
    }

    public DjangoContentType(Integer id, String appLabel, String model) {
        this.id = id;
        this.appLabel = appLabel;
        this.model = model;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getAppLabel() {
        return appLabel;
    }

    public void setAppLabel(String appLabel) {
        this.appLabel = appLabel;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public List<AuthPermission> getAuthPermissionList() {
        return authPermissionList;
    }

    public void setAuthPermissionList(List<AuthPermission> authPermissionList) {
        this.authPermissionList = authPermissionList;
    }

    public List<DjangoAdminLog> getDjangoAdminLogList() {
        return djangoAdminLogList;
    }

    public void setDjangoAdminLogList(List<DjangoAdminLog> djangoAdminLogList) {
        this.djangoAdminLogList = djangoAdminLogList;
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
        if (!(object instanceof DjangoContentType)) {
            return false;
        }
        DjangoContentType other = (DjangoContentType) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.DjangoContentType[ id=" + id + " ]";
    }
    
}
